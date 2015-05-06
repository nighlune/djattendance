/** @jsx React.DOM */

var ATTENDANCE_STATUS_LOOKUP = {
  P: 'present',
  A: 'absent',
  T: 'tardy',
  U: 'uniform',
  L: 'left-class'
};

var SLIP_STATUS_LOOKUP = {
  'A': 'approved',
  'P': 'pending',
  'F': 'fellowship',
  'D': 'denied',
  'S': 'approved'
};

var joinValidClasses = function(classes) {
  return _.compact(classes).join(' ');
};

var WeekBar = React.createClass({displayName: "WeekBar",
  render: function() {
    var startdate = this.props.date.weekday(0).format('M/D/YY');
    var enddate = this.props.date.weekday(6).format('M/D/YY');
    return (
      React.createElement("div", {className: "btn-toolbar", role: "toolbar"}, 
        React.createElement("div", {className: "controls btn-group"}, 
          React.createElement("button", {className: "btn btn-info"}, React.createElement("span", {className: "glyphicon glyphicon-calendar"}))
        ), 
        React.createElement("div", {className: "controls btn-group"}, 
          React.createElement("button", {className: "btn btn-default clndr-previous-button", onClick: actions.prevWeek}, "Prev"), 
          React.createElement("div", {className: "daterange btn btn-default disabled"}, 
            startdate, " to ", enddate
          ), 
          React.createElement("button", {className: "btn btn-default clndr-next-button", onClick: actions.nextWeek}, "Next")
        )
      )
    );
  }
});

var DaysRow = React.createClass({displayName: "DaysRow",
  render: function() {
    var days = [];
    for(var i = 0; i < 7; i++) {
      var name = this.props.date.day(i).format('ddd');
      var num = this.props.date.day(i).format('M/D');
      var isToday = this.props.date.day(i).isSame(moment(), 'day');
      var today = isToday ? 'today' : '';
      var classes = joinValidClasses(['schedule-header', today]);
      days.push(
        React.createElement("div", {className: "col-md-1 no-padding"}, 
          React.createElement("div", {className: classes}, 
            name, " ", React.createElement("br", null), 
            num
          )
        )
      );
    }
    return (
      React.createElement("div", null, 
        React.createElement("div", {className: "col-md-1"}, 
          React.createElement("div", {className: "col-md-1 no-padding"}, 
            React.createElement("div", {className: "schedule-header dead-space"})
          )
        ), 
        days
      )
    );
  }
});


var EventView = React.createClass({displayName: "EventView",
  render: function() {
    console.log('render event', this.props.event.attributes.start);
    var ev = this.props.event;
    var roll = this.props.rolls.get(ev.get('roll'));
    var status = roll ? ATTENDANCE_STATUS_LOOKUP[roll.get('status')] : '';
    var todayClass = (ev.id === 'TODAY') ? 'today-marker' : '';
    var leaveslip = this.props.slips.get(ev.get('slip'));
    var slipStatus = leaveslip ? leaveslip.get('status') : '';
    var classes = joinValidClasses(['schedule-event', status, SLIP_STATUS_LOOKUP[slipStatus], todayClass, ev.get('selected')]);
    //ev.get('rolls').at(ev.get('rolls').length - 1).get('roll')
    var divStyle = {
      top: moment.duration(moment(ev.get('start')).format('H:m')).subtract(6, 'hours').asMinutes()/2,
      height: moment(ev.get('end')).diff(moment(ev.get('start')), 'minutes')/2
    };
    return(
      React.createElement("div", {className: classes, onClick: actions.toggleEvent(this.props.event), style: divStyle, "data-id": ev.get('id'), "data-roll": ev.get('roll_id')}, 
        ev.get('code'), 
        React.createElement("div", {className: "slip-event-status"}, SLIP_STATUS_LOOKUP[slipStatus])
      )
    );
  }
});

var EventGrid = React.createClass({displayName: "EventGrid",
  render: function() {
    var cols = [],
        weekStart = moment(this.props.date).startOf('week'),
        weekEnd = moment(this.props.date).endOf('week'),
        now = moment();
    //get events only from the state's week
    var week_events = this.props.events.filter(function(ev) {
      return (weekStart < moment(ev.get('start')) && weekEnd > moment(ev.get('end')));
    }, this);

    // If today is within current week, add the event marker
    if (weekStart < now && weekEnd > now) {
      var todayEventMarker = new Event({
        id: 'TODAY',
        selected: '',
        start: moment(),
        end: moment()
      });

      week_events.push(todayEventMarker);
    }

    if(this.isMounted()) {
      this.props.setWeekEvents(week_events);
    }

    console.log(week_events, this.props.events.models);

    for(var i = 0; i < 7; i++) {
      //get events for one day
      var day_events = _.filter(week_events, function(ev) {
        return moment(ev.get('start')).weekday() === i; // this == i
      });

      var day_col = [];
      day_events.forEach(function(event) {
        day_col.push(React.createElement(EventView, {event: event, slips: this.props.slips, rolls: this.props.rolls, selectEvent: this.props.selectEvent, key: event.id}));
      }, this);

      var isToday = this.props.date.day(i).isSame(now, 'day');
      var today = isToday ? 'today' : '';
      var classes = joinValidClasses(['day event-col col-md-1 no-padding', today]);
      cols.push(React.createElement("div", {key: i, className: classes}, day_col));
    }
    return (
      React.createElement("div", null, 
        cols
      )
    );
  }
});


var Time = React.createClass({displayName: "Time",
  render: function() {
    var hour = moment().hour(this.props.hour).format('h A');
    return(
      React.createElement("div", {className: "hour"}, 
        React.createElement("div", {className: "hour-text"}, hour)
      )
    );
  }
});

var TimesColumn = React.createClass({displayName: "TimesColumn",
  render: function() {
    var times = [];
    for(var i = 6; i < 24; i++) {
      times.push(React.createElement(Time, {hour: i}));
    }
    return (
      React.createElement("div", {className: "col-md-1 timebar"}, 
        times
      )
    );
  }
});

var Leaveslip = React.createClass({displayName: "Leaveslip",
  getInitialState:function(){
      return {
        type: '',
        comments: '',
        description: '',
        texted: false,
        informed: false
      }
  },
  render: function() {
    var slip = this.props.slip,
        comments = slip.get('comments'),
        comments = (comments && comments !== '') ? comments : (React.createElement("i", null, "No Comments")),
        description = slip.get('description'),
        description = (description && description !== '') ? description : (React.createElement("i", null, "No Description")),
        status = SLIP_STATUS_LOOKUP[slip.get('status')],
        titleClasses = joinValidClasses(['list-group-item active', status]);
    return (
      React.createElement("div", {className: "leaveslip-container"}, 
        React.createElement("div", {className: "list-group"}, 
          React.createElement("a", {href: "#", className: titleClasses}, 
            slip.get('type'), 
            React.createElement("span", {className: "badge"}, status)
          ), 
          React.createElement("div", {className: "list-group-item"}, description), 
          React.createElement("div", {className: "list-group-item"}, comments)
        )
      )
    );
  }
});

var Leaveslips = React.createClass({displayName: "Leaveslips",
  render: function() {
    var selectedSlips = this.props.selectedSlips,
        slips = [],
        i, _len;

    for (i = 0, _len = this.props.selectedSlips.length; i < _len; i++) {
      slips.push(React.createElement(Leaveslip, {slip: selectedSlips[i]}));
    }

    if (slips.length === 0) {
      slips = (
        React.createElement("div", null, 
          React.createElement("i", null, "No event(s) with leaveslip(s) selected"), 
          React.createElement("div", {className: "form-group center-padded"}, 
            React.createElement("button", {className: "btn btn-primary"}, React.createElement("span", {className: "glyphicon glyphicon-pencil"}), " Write New Leaveslip")
          )
        )
      );
    }

    console.log('selected slips', selectedSlips);
    return (
      React.createElement("div", {className: "panel panel-default", id: "submit-leaveslip"}, 
        React.createElement("div", {className: "panel-heading"}, 
          React.createElement("h3", {className: "panel-title", id: "event-title"}, "Leave Slip(s)")
        ), 
        React.createElement("div", {className: "panel-body event-info leaveslip-info"}, 
          slips
        )
      )
    );
  }
});

var RollView = React.createClass({displayName: "RollView",
  setRoll: function(ev) {
    console.log('setRoll', arguments, this);
    var btn = ev.target;
    var status = (btn.id.charAt(0)).toUpperCase();
    this.props.setRollStatus(status);

    if (btn.id === 'present') {
      console.log('present');
    } else if (btn.id === 'absent') {
      console.log('absent');
    } else if (btn.id === 'tardy') {
      console.log('tardy');
    } else if (btn.id === 'uniform') {
      console.log('uniform');
    } else if (btn.id === 'left-class') {
      console.log('left-class');
    } else {
      console.log('not recognized button');
    }
  },
  render: function() {
    var disabled = _.size(this.props.selectedEvents) <= 0,
        rollPane;

    if (!disabled) {
      rollPane = (
        React.createElement("div", null, 
          React.createElement("button", {id: "present", type: "button", onClick: actions.setRoll, className: "btn btn-default btn-block", disabled: disabled}, "Present"), 
          React.createElement("button", {id: "absent", type: "button", onClick: actions.setRoll, className: "btn btn-danger btn-block", disabled: disabled}, "Absent"), 
          React.createElement("button", {id: "tardy", type: "button", onClick: actions.setRoll, className: "btn btn-warning btn-block", disabled: disabled}, "Tardy"), 
          React.createElement("button", {id: "uniform", type: "button", onClick: actions.setRoll, className: "btn btn-warning btn-block", disabled: disabled}, "Uniform"), 
          React.createElement("button", {id: "left-class", type: "button", onClick: actions.setRoll, className: "btn btn-warning btn-block", disabled: disabled}, "Left Class")
        )
      );
    } else {
      rollPane = (
        React.createElement("span", {className: "info-message"}, "Please select event(s) to record attendance")
      );
    }

    return (
      React.createElement("div", {className: "panel panel-default", id: "submit-roll"}, 
        React.createElement("div", {className: "panel-heading"}, 
          React.createElement("h3", {className: "panel-title", id: "event-title"}, "Submit Roll")
        ), 
        React.createElement("div", {className: "panel-body event-info"}, 
          rollPane
        )
      )
    );
  }
});

// working on viewing the leaveslips *not working*

// var slipsBar = React.createClass({
//   render: function() {
//     var selectedSlips = this.props.selectedSlips,
//         slips = [],
//         i, _len;

//     for (i = 0, _len = this.props.selectedSlips.length; i < _len; i++) {
//       slips.push(<Leaveslip slip={selectedSlips[i]} />);
//     }

//     if (slips.length === 0) {
//       slips = (
//         <div>
//           <i>No event(s) with leaveslip(s) selected</i>
//           <div className="form-group center-padded">
//             <button className="btn btn-primary"><span className="glyphicon glyphicon-pencil"></span> Write New Leaveslip</button>
//           </div>
//         </div>
//       );
//     }
//     return (
//       <div className="panel panel-default leaveslip-container">
//         <div className="list-group">
//           <a href="#" className={titleClasses}>
//             {slip.get('type')}
//             <span className="badge">{status}</span>
//           </a>
//           <div className="list-group-item">{description}</div>
//           <div className="list-group-item">{comments}</div>
//         </div>
//       </div>
//     );
//   }
// });
