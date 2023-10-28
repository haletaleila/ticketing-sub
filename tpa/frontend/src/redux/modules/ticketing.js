import Cookies from 'js-cookie';;
const SET_BLOCKOBJ = "SET_BLOCKOBJ";
const SET_RANDOMOBJ = "SET_RANDOMOBJ";
function setBlockObj(blockobj) {
  return {
    type: SET_BLOCKOBJ,
    blockobj,
  };
}
function setRandomObj(randomobj) {
  return {
    type: SET_RANDOMOBJ,
    randomobj,
  };
}
// API Actions
function getBaseballBlockObj(eng) {
  return (dispatch, getState) => {
    fetch("/ticketing/api/baseball/info/?eng="+eng, {
    })
      .then(response => {
        return response.json();
      })
      .then(json => {
        dispatch(setBlockObj(json));
      })
  };
}
function getRandomTicketLink() {
  return (dispatch, getState) => {
    fetch("/ticketing/api/randomtl/", {
    })
      .then(response => {
        return response.json();
      })
      .then(json => {
        dispatch(setRandomObj(json));
      })
  };
}
function getFootballBlockObj(eng) {
  return (dispatch, getState) => {
    fetch("/ticketing/api/football/info/?eng="+eng, {
    })
      .then(response => {
        return response.json();
      })
      .then(json => {
        dispatch(setBlockObj(json));
      })
  };
}
// Initial State

const initialState = {};

// Reducer

function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_BLOCKOBJ:
      return applySetBlockObj(state, action);
    case SET_RANDOMOBJ:
      return applySetRandomObj(state, action);
    default:
      return state;
  }
}
// Reducer Functions
function applySetBlockObj(state, action) {
  const { blockobj } = action;
  return {
    ...state,
    blockobj
  };
}
function applySetRandomObj(state, action) {
  const { randomobj } = action;
  return {
    ...state,
    randomobj
  };
}
const actionCreators = {
  getBaseballBlockObj,
  getFootballBlockObj,
  getRandomTicketLink,
};

export { actionCreators };

// Export reducer by default

export default reducer;