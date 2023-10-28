import React, { Component } from "react";
import PropTypes from "prop-types";
import Footer from "./presenter";
import { useEffect } from 'react'

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
class Container extends Component {
  state = {
  };
  static propTypes = {
  };
  componentDidMount() {
  };
  componentWillReceiveProps = nextProps => {
   
  }
 
  render() {
    const { pathname} = this.props;
    return (
      <Footer pathname={pathname}{...this.state} {...this.props}/>
    );
  }

}

export default Container;