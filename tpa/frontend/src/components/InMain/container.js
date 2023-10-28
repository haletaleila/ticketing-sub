import React, { Component } from "react";
import PropTypes from "prop-types";
import axios from "axios";
import InLeftNav from "../InLeftNav/presenter";
import InRightNav from "../InRightNav/presenter";
import { useParams, Router, Link } from "react-router-dom";
import InMain from "./presenter";
class Container extends Component {
  state = {
    selectedSeats: [],
  };

  handleConfirmSelection = () => {
    alert("선택 완료됐습니다");
    this.setState({ selectedSeats: [] }, () => {
      window.location.reload();
    }); // 상태 초기화 후 페이지 새로고침
  };

  handleSeatSelection = (selectedSeats) => {
    this.setState({ selectedSeats });
  };

  static propTypes = {};
  componentWillReceiveProps = (nextProps) => {};

  componentDidMount() {
    document.title = "인터파크 메인";
  }

  render() {
    const { selectedSeats } = this.state;
    return (
      <InMain
        onSeatSelection={this.handleSeatSelection}
        onConfirm={this.handleConfirmSelection} // onConfirm prop으로 메소드 전달
        selectedSeats={selectedSeats}
      />
    );
  }
}

export default Container;
