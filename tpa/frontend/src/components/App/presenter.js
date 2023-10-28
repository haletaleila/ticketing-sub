import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";
import { Route, Switch, Redirect, withRouter } from "react-router";
import "./styles.module.scss";
import TlBaseball from "../TlBaseball";
import TlFootball from "../TlFootball";
import TrandomGame from "../TrandomGame";
import Main from "../Main";
import { connect } from "react-redux";
import Preparing from "../Preparing";
import TopNav from "../TopNav";
import Footer from "../Footer";
import CaptchaGame from "../CaptchaGame";
import Physical from "../Physical";
import InMain from "../InMain";

const App = (props) => {
  const [windowDimensions, setWindowDimensions] = useState({
    width: window.innerWidth,
    height: window.innerHeight,
  });

  useEffect(() => {
    function handleResize() {
      setWindowDimensions({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    }

    window.addEventListener("resize", handleResize);

    // Cleanup event listener on component unmount
    return () => window.removeEventListener("resize", handleResize);
  }, []); // Empty dependency array ensures this runs on mount and unmount only

  const { width, height } = windowDimensions;

  return (
    <>
      {width < 980 || height < 600 ? (
        <Route path="/" component={Preparing} key={1} />
      ) : (
        <>
          <Route path="/" component={TopNav} key={1} />
          <Switch>
            <Route path="/tlbaseball" component={TlBaseball} key={2} />
            <Route path="/physical" component={Physical} key={3} />
            <Route path="/tlrandomgame" component={TrandomGame} key={3} />
            <Route path="/captcha" component={CaptchaGame} key={3} />
            <Route path="/tlfootball" component={TlFootball} key={4} />
            <Route path="/inmain/:category" component={InMain} key={5} />
            <Route path="/" component={Main} key={6} exact />{" "}
            {/* 'exact' prop added to avoid conflicts */}
          </Switch>
          <Route path="/" component={Footer} key={7} />
        </>
      )}
    </>
  );
};

App.propTypes = {
  // your propTypes here
};

export default withRouter(connect()(App));
