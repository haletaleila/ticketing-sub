import React from "react";
import PropTypes from "prop-types";
import { Router, Link } from "react-router-dom";
import styles from "./styles.module.scss";
import { TypeAnimation } from "react-type-animation";
const InRightNav = ({ selectedSeats, onConfirm }) => {
  return (
    <>
      <div class="seatR">
        <div class="inner">
          <div class="seat_select1">
            <h3 class="title">
              <img
                src="//ticketimage.interpark.com/TicketImage/onestop/stit_seat_02.gif"
                alt="선택좌석"
              />
            </h3>
            <span class="ea">
              총&nbsp;
              <span id="SelectedSeatCount" name="SelectedSeatCount">
                {selectedSeats.length}
              </span>
              석 선택되었습니다.
            </span>
            <div class="seat_choice">
              <table class="seat1">
                <colgroup>
                  <col width="75px" />
                  <col width="*" />
                </colgroup>
                <tbody>
                  <tr>
                    <th>좌석등급</th>
                    <td>좌석번호</td>
                  </tr>
                </tbody>
              </table>
              <div class="choice">
                <div class="scrollY">
                  <div id="SelectedSeat" name="SelectedSeat">
                    <table class="seat2">
                      <colgroup>
                        <col width="75px" />
                        <col width="*" />
                      </colgroup>
                      <tbody>
                        {selectedSeats.map((seat, index) => (
                          <tr key={index}>
                            <td>{seat.grade}</td>
                            <td>{`${seat.rowNumber}-${seat.position}번석`}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
            <div class="btnWrap">
              <a href="javascript:;" onClick={onConfirm}>
                <img
                  id="NextStepImage"
                  src="http://ticketimage.interpark.com/TicketImage/onestop/btn_seat_confirm.gif"
                  alt="좌석선택완료"
                />
              </a>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
InRightNav.propTypes = {
  selectedSeats: PropTypes.array.isRequired,
  onConfirm: PropTypes.func.isRequired,
};

export default InRightNav;
