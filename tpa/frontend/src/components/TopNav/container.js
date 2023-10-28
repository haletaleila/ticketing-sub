import React, { Component } from "react";
import PropTypes from "prop-types";
import TopNav from "./presenter";
import { useEffect } from 'react'

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
class Container extends Component {
  state = {
  };
  static propTypes = {
  };
  componentDidMount() {
    const { isLoggedIn, nickname} = this.props;
    this.setState({
      loginStatus : isLoggedIn,
      mynick : nickname,
    })
  };
  componentWillReceiveProps = nextProps => {
   
  }
 
  render() {
    const { pathname} = this.props;
    return (
      <TopNav pathname={pathname}{...this.state} {...this.props}/>
    );
  }

}

export default Container;