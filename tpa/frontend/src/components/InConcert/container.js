import React, { Component } from "react";
import PropTypes from "prop-types";
import InConcert from "./presenter";
import axios from "axios";
import data from "../../json/innerseat-248.json";
class Container extends Component {
  state = {
    data: data,
  };

  static propTypes = {};
  componentWillReceiveProps = (nextProps) => {};
  // 백단 api 호출 시 state에 넣어주기 위해서
  //

  componentDidMount() {
    document.title = "인터파크 콘서트";
    console.log(data);
  }
  render() {
    return (
      <>
        <InConcert
          handleFocus={this.handleFocus}
          reload={this.reload}
          handleChange={this.handleChange}
          handleKeyDown={this.handleKeyDown}
          {...this.state}
        />
      </>
    );
  }
}

export default Container;
