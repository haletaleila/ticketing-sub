import Cookies from 'js-cookie';;
const SET_CARD = "SET_CARD";
function setCard(card) {
  return {
    type: SET_CARD,
    card,
  };
}
// API Actions
function getCard(eng) {
  return (dispatch, getState) => {
    fetch("/card/api/info/", {
    })
      .then(response => {
        return response.json();
      })
      .then(json => {
        dispatch(setCard(json));
      })
  };
}
// Initial State

const initialState = {};

// Reducer

function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_CARD:
      return applySetCard(state, action);
    default:
      return state;
  }
}
// Reducer Functions
function applySetCard(state, action) {
  const { card } = action;
  return {
    ...state,
    card
  };
}
const actionCreators = {
  getCard,
};

export { actionCreators };

// Export reducer by default

export default reducer;