import React from "react";
import PropTypes from "prop-types";
import { Router, Link } from "react-router-dom";
import styles from "./styles.module.scss";
import { TypeAnimation } from "react-type-animation";

const InLeftNav = ({ props }) => {
  return (
    <div className={styles["left-nav"]}>
      {props.categoryData
        ? props.categoryData.map((item) => (
            <div key={item.id} onClick={() => props.onConcertClick(item)}>
              {item.name}
            </div>
          ))
        : "No data for this category"}

      {props.selectedConcertVisible &&
        props.selectedConcert &&
        props.selectedConcert.selector === "2" && (
          <div>
            <table
              width="100%"
              height="100%"
              cellpadding="0"
              cellspacing="0"
              id="TmgsTable"
              name="TmgsTable"
            >
              <tbody>
                <tr>
                  <td valign="top" style={{ padding: "20px" }} nowrap="true">
                    <table
                      width="600"
                      border="0"
                      cellspacing="0"
                      cellpadding="0"
                    >
                      <tbody>
                        <tr>
                          <td
                            className={styles.TableTbodyTrTd}
                            width="4"
                            height="4"
                          >
                            <img
                              src="//ticketimage.interpark.com/TicketImage/event/061227/seat_nt_left_01.gif"
                              width="4"
                              height="4"
                            />
                          </td>
                          <td
                            className={styles.TableTbodyTrTd}
                            height="4"
                            background="http://ticketimage.interpark.com/TicketImage/event/061227/seat_nt_top.gif"
                          ></td>
                          <td
                            className={styles.TableTbodyTrTd}
                            width="4"
                            height="4"
                          >
                            <img
                              src="//ticketimage.interpark.com/TicketImage/event/061227/seat_nt_right_01.gif"
                              width="4"
                              height="4"
                            />
                          </td>
                        </tr>
                        <tr>
                          <td
                            className={styles.TableTbodyTrTd2}
                            width="4"
                            background="http://ticketimage.interpark.com/TicketImage/event/061227/seat_nt_left_bg.gif"
                          ></td>
                          <td
                            className={styles.TableTbodyTrTd2}
                            bgcolor="#EBEBEB"
                          >
                            <img
                              src="//ticketimage.interpark.com/TicketImage/event/061227/dot_03.gif"
                              width="5"
                              height="5"
                              align="absmiddle"
                            />{" "}
                            원하시는 영역을 선택해주세요. 공연장에서 위치를
                            클릭하거나, 오른쪽의 좌석을 선택해주세요.
                          </td>
                          <td
                            className={styles.TableTbodyTrTd2}
                            width="4"
                            background="http://ticketimage.interpark.com/TicketImage/event/061227/seat_nt_right_bg.gif"
                          ></td>
                        </tr>
                        <tr>
                          <td
                            className={styles.TableTbodyTrTd}
                            width="4"
                            height="4"
                          >
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
                          <td
                            className={styles.TableTbodyTrTd}
                            width="4"
                            height="4"
                          >
                            <img
                              src="//ticketimage.interpark.com/TicketImage/event/061227/seat_nt_right_02.gif"
                              width="4"
                              height="4"
                            />
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <br />

                    <title>08000885</title>
                    <meta
                      http-equiv="Content-Type"
                      content="text/html; charset=euc-kr"
                    />

                    <img
                      src="http://ticketimage.interpark.com/TMGSNAS/TMGS/MiniMapHtml/23/img/23001192.gif"
                      alt=""
                      width="600"
                      height="540"
                      border="0"
                      usemap="#Map"
                    />
                    <map name="Map">
                      {props.selectedConcert.getData.outerSelect.map((area) => (
                        <area
                          key={area.id}
                          shape={area.shape}
                          coords={area.coords}
                          alt={area.id}
                          onFocus="this.blur()"
                          style={{ cursor: "pointer" }}
                          onClick={() => props.onAreaClick(area)}
                        />
                      ))}
                    </map>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        )}

      {props.selectedAreaVisible && props.selectedArea && (
        <div>
          <table
            className={styles.tmgsTable}
            width="100%"
            height="100%"
            cellpadding="0"
            cellspacing="0"
          >
            <tbody>
              <tr>
                <td valign="top" style={{ padding: "20px" }} nowrap="true">
                  <div className={styles.divSeatBox}>
                    <table
                      width="600"
                      border="0"
                      cellspacing="0"
                      cellpadding="0"
                    >
                      <tbody>
                        <tr>
                          <td
                            className={styles.TableTbodyTrTd}
                            width="4"
                            height="4"
                          >
                            <img
                              src="//ticketimage.interpark.com/TicketImage/event/061227/seat_nt_left_01.gif"
                              width="4"
                              height="4"
                            />
                          </td>
                          <td
                            className={styles.TableTbodyTrTd}
                            height="4"
                            background="http://ticketimage.interpark.com/TicketImage/event/061227/seat_nt_top.gif"
                          ></td>
                          <td
                            className={styles.TableTbodyTrTd}
                            width="4"
                            height="4"
                          >
                            <img
                              src="//ticketimage.interpark.com/TicketImage/event/061227/seat_nt_right_01.gif"
                              width="4"
                              height="4"
                            />
                          </td>
                        </tr>
                        <tr>
                          <td
                            className={styles.TableTbodyTrTd2}
                            width="4"
                            background="http://ticketimage.interpark.com/TicketImage/event/061227/seat_nt_left_bg.gif"
                          ></td>
                          <td
                            className={styles.TableTbodyTrTd}
                            bgcolor="#EBEBEB"
                          >
                            <img
                              src="//ticketimage.interpark.com/TicketImage/event/061227/dot_03.gif"
                              width="5"
                              height="5"
                              align="absmiddle"
                            />{" "}
                            <b>
                              <font color="#3300FF">
                                {props.selectedArea.sectionRealName} 영역
                              </font>
                              의 좌석배치도입니다
                            </b>
                          </td>
                          <td
                            className={styles.TableTbodyTrTd2}
                            width="4"
                            background="http://ticketimage.interpark.com/TicketImage/event/061227/seat_nt_right_bg.gif"
                          ></td>
                        </tr>
                        <tr>
                          <td
                            className={styles.TableTbodyTrTd}
                            width="4"
                            height="4"
                          >
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
                          <td
                            className={styles.TableTbodyTrTd}
                            width="4"
                            height="4"
                          >
                            <img
                              src="//ticketimage.interpark.com/TicketImage/event/061227/seat_nt_right_02.gif"
                              width="4"
                              height="4"
                            />
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <table
                      width="600"
                      border="0"
                      cellspacing="0"
                      cellpadding="0"
                    >
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
                    {props.selectedArea.rows.map((row, rowIndex) => (
                      <>
                        <div className={styles.divBr}>
                          <span
                            className={styles.span}
                            align="left"
                            style={{ width: "100px", paddingLeft: "5px" }}
                          >
                            <font
                              style={{ fontSize: "8pt", color: "#636363" }}
                              face="굴림"
                              align="left"
                            >
                              {`${props.selectedArea.sectionName} ${row.rowNumber}`}
                            </font>
                          </span>
                          {row.seats.map((seat, seatIndex) => (
                            <span
                              className={
                                seat.type === "R" ? styles.seatR : styles.seatB
                              }
                              onClick={() =>
                                props.onSeatClick(row.rowNumber, seat)
                              }
                              style={
                                props.selectedSeats &&
                                props.selectedSeats.some(
                                  (selectedSeat) =>
                                    selectedSeat.identifier ===
                                    `${row.rowNumber}-${seat.position}`
                                )
                                  ? { backgroundColor: "black" }
                                  : {}
                              }
                            />
                          ))}
                        </div>
                        {Array.from({ length: row.breakAfter }, (_, i) => (
                          <br key={i} />
                        ))}
                      </>
                    ))}
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};
InLeftNav.propTypes = {
  categoryData: PropTypes.array.isRequired,
  selectedConcert: PropTypes.object,
  onConcertClick: PropTypes.func.isRequired,
  onAreaClick: PropTypes.func.isRequired,
  selectedArea: PropTypes.array,
  selectedSeats: PropTypes.array,
};

export default InLeftNav;
