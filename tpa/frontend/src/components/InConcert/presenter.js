import React from "react";
import PropTypes from "prop-types";
import { Router, Link } from "react-router-dom";
import styles from "./styles.module.scss";
import { TypeAnimation } from "react-type-animation";
const InConcert = (props, context) => (
  <>
    <table
      width="100%"
      height="100%"
      cellpadding="0"
      cellspacing="0"
      className={styles.TmgsTable}
    >
      <tbody>
        <tr>
          <td valign="top" style={{ padding: "20px" }} nowrap="true">
            <div className={styles.DivSeatBox}>
              <table width="600" border="0" cellspacing="0" cellpadding="0">
                <tbody>
                  <tr>
                    <td width="4" height="4" className={styles.TableTbodyTrTd}>
                      <img
                        src="//ticketimage.interpark.com/TicketImage/event/061227/seat_nt_left_01.gif"
                        width="4"
                        height="4"
                      />
                    </td>
                    <td
                      height="4"
                      background="http://ticketimage.interpark.com/TicketImage/event/061227/seat_nt_top.gif"
                      className={styles.TableTbodyTrTd}
                    ></td>
                    <td width="4" height="4" className={styles.TableTbodyTrTd}>
                      <img
                        src="//ticketimage.interpark.com/TicketImage/event/061227/seat_nt_right_01.gif"
                        width="4"
                        height="4"
                      />
                    </td>
                  </tr>
                  <tr>
                    <td
                      width="4"
                      background="http://ticketimage.interpark.com/TicketImage/event/061227/seat_nt_left_bg.gif"
                      className={styles.TableTbodyTrTd2}
                    ></td>
                    <td bgcolor="#EBEBEB">
                      <img
                        src="//ticketimage.interpark.com/TicketImage/event/061227/dot_03.gif"
                        width="5"
                        height="5"
                        align="absmiddle"
                        className={styles.TableTbodyTrTd2}
                      />
                      <b>
                        <font color="#3300FF">{props.sector} 영역</font>의
                        좌석배치도입니다
                      </b>
                    </td>
                    <td
                      className={styles.TableTbodyTrTd2}
                      width="4"
                      background="http://ticketimage.interpark.com/TicketImage/event/061227/seat_nt_right_bg.gif"
                    ></td>
                  </tr>
                  <tr>
                    <td width="4" height="4" className={styles.TableTbodyTrTd}>
                      <img
                        src="//ticketimage.interpark.com/TicketImage/event/061227/seat_nt_left_02.gif"
                        width="4"
                        height="4"
                      />
                    </td>
                    <td
                      className={styles.TableTbodyTrTd}
                      height="4"
                      background="http://ticketimage.interpark.com/TicketImage/event/061227/seat_nt_bottom.gif"
                    ></td>
                    <td width="4" height="4" className={styles.TableTbodyTrTd}>
                      <img
                        src="//ticketimage.interpark.com/TicketImage/event/061227/seat_nt_right_02.gif"
                        width="4"
                        height="4"
                      />
                    </td>
                  </tr>
                </tbody>
              </table>
              <table width="600" border="0" cellspacing="0" cellpadding="0">
                <tbody>
                  <tr>
                    <td height="10"></td>
                  </tr>
                  <tr>
                    <td>
                      <img
                        src="http://ticketimage.interpark.com/TicketImage/onestop/html/default.gif"
                        onerror="javascript:this.src='http://ticketimage.interpark.com/TicketImage/onestop/html/default.gif'"
                      />
                    </td>
                  </tr>
                </tbody>
              </table>
              {props.data.map((section, sectionIndex) => (
                <div key={sectionIndex}>
                  {section.rows.map((row, rowIndex) => (
                    <>
                      <div className={styles.DivBr}>
                        <span
                          className={styles.SeatT}
                          align="left"
                          style={{ width: "100px", paddingLeft: "5px" }}
                        >
                          <font
                            style={{ fontSize: "8pt", color: "#636363" }}
                            face="굴림"
                            align="left"
                          >
                            {`${section.sectionName} ${row.rowNumber}`}
                          </font>
                        </span>
                        {row.seats.map((seat, seatIndex) => (
                          <>
                            {seat.type === "R" ? (
                              <span
                                className={styles.SeatR}
                                // style={{
                                //   ...props.selectedSeatsStyles[
                                //     JSON.stringify({
                                //       ...props.sector,
                                //       sectionName: section.sectionName,
                                //       rowNumber: row.rowNumber,
                                //       position: seat.position,
                                //     })
                                //   ],
                                //   ...(props.selectedSeatsStyles[
                                //     JSON.stringify({
                                //       sector,
                                //       sectionName: section.sectionName,
                                //       rowNumber: row.rowNumber,
                                //       position: seat.position,
                                //     })
                                //   ]
                                //     ? {}
                                //     : { backgroundColor: seat.color }),
                                // }}
                                onClick={() =>
                                  props.handleSeatClick(
                                    seat,
                                    section.sectionName,
                                    row.rowNumber
                                  )
                                }
                              />
                            ) : (
                              <span />
                            )}
                          </>
                        ))}
                      </div>
                      {Array.from({ length: row.breakAfter }, (_, i) => (
                        <br key={i} />
                      ))}
                    </>
                  ))}
                </div>
              ))}
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </>
);
InConcert.propTypes = {
  handleChange: PropTypes.func.isRequired,
  handleKeyDown: PropTypes.func.isRequired,
  reload: PropTypes.func.isRequired,
  handleFocus: PropTypes.func.isRequired,
  inputValue: PropTypes.string.isRequired,
  time: PropTypes.number.isRequired,
  isTimer: PropTypes.bool.isRequired,
  score: PropTypes.number.isRequired,
};

export default InConcert;
