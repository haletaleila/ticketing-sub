import { combineReducers, createStore, applyMiddleware } from "redux";
import { routerMiddleware } from "connected-react-router";
import { composeWithDevTools } from "redux-devtools-extension";
import { connectRouter } from "connected-react-router";
import createHistory from "history/createBrowserHistory";
import thunk from "redux-thunk";
import ticketing from "../redux/modules/ticketing";
import card from "../redux/modules/card";
import user from "../redux/modules/user";
import category from "../redux/modules/incategory"; // Import the new module
import { i18nState } from "redux-i18n";

const env = process.env.NODE_ENV;

const history = createHistory();

const middlewares = [thunk, routerMiddleware(history)];

if (env === "development") {
  const { logger } = require("redux-logger");
  middlewares.push(logger);
}

const reducer = combineReducers({
  ticketing,
  user,
  card,
  i18nState,
  category,
  router: connectRouter(history),
});

let store;

if (env === "development") {
  store = (initialState) =>
    createStore(reducer, composeWithDevTools(applyMiddleware(...middlewares)));
} else {
  store = (initialState) =>
    createStore(reducer, applyMiddleware(...middlewares));
}

export { history };

export default store();
