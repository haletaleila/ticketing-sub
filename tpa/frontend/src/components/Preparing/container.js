import React, { Component } from "react";
import PropTypes from "prop-types";
import Preparing from "./presenter";

class Container extends Component {
  state = {
    
  };
  
  static propTypes = {
   
  };
  componentWillReceiveProps = nextProps => {
    
  }
  componentDidMount() {
    document.title = "티켓랩(TicketLab) 미지원 기기";
  };
  render() {
    return (
      <>
      <Preparing {...this.state}/>
      </>
    );
  }
}

export default Container;