import React, { Component } from "react";
import PropTypes from "prop-types";
import axios from "axios";
import InLeftNav from "./presenter";
import data from "./json/data.json";

class Container extends Component {
  state = {
    data: data,
    selectedConcert: null,
    selectedArea: null,
    selectedConcertVisible: true, // 초기에는 true로 설정
    selectedAreaVisible: true,
    category: "", // 초기에는 빈 문자열로 설정
    selectedSeats: [],
  };

  static propTypes = {
    category: PropTypes.string.isRequired, // category prop의 유형을 지정합니다.
    selectedArea: PropTypes.object,
  };

  handleConfirmSelection = () => {
    this.props.onConfirm(); // 상위 컴포넌트의 handleConfirmSelection 메소드 호출
  };

  // InLeftNav 컴포넌트의 handleSeatClick 메서드를 업데이트
  handleSeatClick = (rowNumber, seat, sectionName, sectionRealName) => {
    const identifier = `${rowNumber}-${seat.position}`;
    this.setState((prevState) => {
      const selectedSeats = [...prevState.selectedSeats];
      const seatIndex = selectedSeats.findIndex(
        (seat) => seat.identifier === identifier
      );

      if (seatIndex !== -1) {
        selectedSeats.splice(seatIndex, 1);
      } else {
        const selectedSeatData = {
          identifier,
          rowNumber,
          position: seat.position,
          grade: seat.grade,
          sectionName,
          sectionRealName,
        };
        selectedSeats.push(selectedSeatData);
      }

      // 상태 변경을 InMain 컴포넌트에 알립니다.
      this.props.onSeatSelection(selectedSeats);
      return { selectedSeats };
    });
  };

  onAreaClick = (area, sectionName, sectionRealName) => {
    const selectedArea = this.state.selectedConcert.getData.innerSelect.find(
      (innerSelect) => innerSelect.sectionRealName === area.id
    );
    this.setState({ selectedArea });
    this.setState({ selectedConcertVisible: false });
    this.setState({ selectedAreaVisible: true });
  };

  handleConcertClick = (concert) => {
    this.setState({ selectedConcertVisible: true });
    this.setState({ selectedAreaVisible: false });
    this.setState({ selectedConcert: concert });
  };

  componentWillReceiveProps(nextProps) {
    if (nextProps.onConfirm !== this.props.onConfirm) {
      this.setState({ selectedSeats: [] }); // 상태 초기화
    }
  }

  componentDidMount() {
    document.title = "인터파크 레프트";
    const lastSegment = window.location.pathname.split("/").pop();
    this.setState({ category: lastSegment }); // lastSegment를 state에 저장합니다.
  }

  render() {
    const { category, selectedSeats } = this.state; // state에서 category를 가져옵니다.
    const props = {
      categoryData: this.state.data[category],
      selectedConcert: this.state.selectedConcert,
      onConcertClick: this.handleConcertClick,
      onAreaClick: this.onAreaClick,
      selectedArea: this.state.selectedArea,
      selectedConcertVisible: this.state.selectedConcertVisible,
      selectedAreaVisible: this.state.selectedAreaVisible,
      onSeatClick: this.handleSeatClick,
      selectedSeats: selectedSeats,
      onConfirm: this.props.onConfirm,
    };
    return (
      <>
        <InLeftNav
          props={props}
          onConfirm={this.handleConfirmSelection} // onConfirm prop으로 메소드 전달
        />
      </>
    );
  }
}

export default Container;
