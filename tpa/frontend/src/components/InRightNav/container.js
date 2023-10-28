import React, { Component } from "react";
import PropTypes from "prop-types";
import axios from "axios";
import InRightNav from "./presenter";
class Container extends Component {
  static propTypes = {
    selectedSeats: PropTypes.object,
    onConfirm: PropTypes.func.isRequired, // onConfirm prop 추가
  };

  componentWillReceiveProps = (nextProps) => {};
  // 백단 api 호출 시 state에 넣어주기 위해서
  //

  componentDidMount() {
    document.title = "인터파크 라이트";
  }
  render() {
    const { selectedSeats, onConfirm } = this.props;
    return (
      <>
        <InRightNav
          selectedSeats={selectedSeats}
          onConfirm={onConfirm} // onConfirm prop 전달
        />
      </>
    );
  }
}

export default Container;
