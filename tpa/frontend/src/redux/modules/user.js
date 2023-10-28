import Cookies from 'js-cookie';
const SAVE_TOKEN = "SAVE_TOKEN";
const LOGOUT = "LOGOUT";
const SAVE_NICKNAME = "SAVE_NICKNAME";
const SET_STATUS = "SET_STATUS";
function saveToken(token) {
    return {
      type: SAVE_TOKEN,
      token
    };
  }
  function setStatus(status) {
    return {
      type: SET_STATUS,
      status
    };
  }
function saveNickName(nickname) {
return {
    type: SAVE_NICKNAME,
    nickname
};
}
  
  function logout() {
    return {
      type: LOGOUT
    };
  }
function kakaoLogin(access_token) {
    return dispatch => {
      fetch("/users/login/kakao/", {
        method: "POST",
        headers: {
            'X-CSRFToken': Cookies.get("csrftoken"),
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          access_token
        })
      })
        .then(response => response.json())
        .then(json => {
            
          if(json.nickname){
            dispatch(saveNickName(json.nickname));
          }
          if (json.token) {
            dispatch(saveToken(json.token));
          }
        })
    };
  }
  function changenick(nickname) {
    if(nickname.length>20){
        return dispatch => {
            dispatch(setStatus((Math.random()*1000).toString()));
        }
    }
    return (dispatch, getState) => {
      const { user: { token } } = getState();
      fetch("/users/login/changenick/", {
        method: "POST",
        headers: {
            'X-CSRFToken': Cookies.get("csrftoken"),
            'Content-Type': 'application/json',
            'Authorization': token
        },
        body: JSON.stringify({
          nickname
        })
      })
        .then(response => response.json())
        .then(json => {
            if(json.status){
                dispatch(setStatus(json.status));
                if(json.status=="success"){
                    dispatch(saveNickName(json.nickname));
                }
            }
        })
    };
  }
  const initialState = {
    isLoggedIn: localStorage.getItem("jwt") ? true : false,
    token: localStorage.getItem("jwt"),
    nickname : localStorage.getItem("nickname")
  };
  function reducer(state = initialState, action) {
    switch (action.type) {
        case SAVE_TOKEN:
            return applySetToken(state, action);
        case LOGOUT:
            return applyLogout(state, action);
        case SAVE_NICKNAME:
            return applySetNickName(state, action);
        case SET_STATUS:
            return applySetStatus(state, action);
        default:
            return state;
    }
  }
  function applySetToken(state, action) {
    const { token } = action;
    localStorage.setItem("jwt", token);
    return {
      ...state,
      isLoggedIn: true,
      token: token
    };
  }
  function applySetNickName(state, action) {
    const { nickname } = action;
    localStorage.setItem("nickname", nickname);
    return {
      ...state,
      nickname: nickname
    };
  }
  function applySetStatus(state, action) {
    const { status } = action;
    return {
      ...state,
      status
    };
  }
  function applyLogout(state, action) {
    localStorage.removeItem("jwt");
    localStorage.removeItem("nickname");
    return {
      isLoggedIn: false
    };
  }
  
  const actionCreators = {
    kakaoLogin,
    logout,
    changenick
  };

  export { actionCreators };

  // export reducer by default
  
  export default reducer;