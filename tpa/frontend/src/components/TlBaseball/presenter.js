import React, { forwardRef }from 'react';
import PropTypes from "prop-types";
import {Router,Link } from "react-router-dom";
import styles from "./styles.module.scss";


const TlBaseball = (props, context) => (
  <div className={styles.main} style={{ transform: `scale(${props.scale})`}}>
    {props.blockObj.length==0 && (
      <div className={styles.loading} >
            
      </div>
    )}
    {(props.blockObj.length !== 0 && props.istimer === false && props.time==0) && (
      <div className={styles.preparing} onClick={() => props.startTimer()}>
      </div>
    )}
    <div className={styles.reserveContent}>
      
      <div className={styles.leftReserve} >
      {props.popup && (
          <div id="popup" className={styles.popupLayer} onClick={(e) => {
            // e.target이 팝업 레이어 자체인 경우에만 팝업을 닫도록 판별
            if (e.target.classList.contains(styles.popupLayer)) {
              props.popupClose();
            }
          }}>
            <div className={styles.areaTop}>
              <a href="#" className={styles.close} onClick={() => props.popupClose()}>
              </a>
              <strong class={styles.title}>좌석선택유형</strong>
            </div>    
            <div className={styles.areaBottom}>
              
                {props.selectGradeMap.map((grade,index) =>
                  <div className={styles.seatForm}>
                    <p className={styles.seatName}>
                        <span className={styles.seatColor} style={{ background: grade.color }}/>
                        <div className={styles.seatGrade}>
                          {grade.name}
                        </div>
                        
                    </p>
                    <div className={styles.btnArea}>
                    <div className={styles.cellBx}>
                      <span className={styles.cell}>
                        <a href="#" className={styles.bntFull} onClick={(e) => props.btnBlockClick(e,props.selectBlock,grade.gradeId)}>
                          직접선택
                        </a>
                      </span>
                    </div>
                  </div>
              </div>
              )}
            </div>            
        </div>
      )}
        <div className={styles.mainViewTop} style={{opacity: props.popup ? '0.3' : '1'}}>
          <div id="test" className={styles.mainView}>
          </div>
          <div id="seat_option" className={styles.seatOption}>
            <button onClick={props.allView} type="button" id="btn_allview" className={styles.btnAllVeiw} title="공연장 전체보기">
              <span className={styles.binding}>공연장 전체보기</span>

            </button>
          </div>
          <div className={styles.selectSeatInfo}>
              <div className={styles.scrollSeat}>
                  <ul className={styles.lst}>
                    {props.selectSeat.map((seat,index) =>
                          <li className={styles.seat}>
                            {seat.mapInfo}
                          </li>
                    )}
                  </ul>
              </div>
          </div>
        </div>
        
      </div>
      <div className={styles.rightReserve}>
        <div className={styles.artbx}>
          <div className={styles.bxTit}>
            등급 선택
          </div>
          <ul id="select_seat_grade" className={styles.seatList}>
          {Object.keys(props.gradeMap).map((gradeKey, index) => (
            <li key={index}>
              <a href="#" className={styles.gradeSelect} onClick={(e) => props.selectGrade(e,gradeKey)}>

              
              <span className={styles.seatColor} style={{ background: props.gradeMap[gradeKey].color }}>
                {/* 내용 */}
              </span>
              <div className={styles.seatDetailInfo}>
                <span className={styles.seatGrade}>
                  {props.gradeMap[gradeKey].name}
                </span>
              </div>
              </a>
                {props.selectGradeId===gradeKey && props.selectBlockMap.length<=1 && (
                  <div className={styles.btnArea}>
                    <div className={styles.cellBx}>
                      <span className={styles.cell}>
                        <a href="#" className={styles.bntFull} onClick={(e) => props.btnGradeClick(e,gradeKey)}>
                          직접선택
                        </a>
                      </span>
                    </div>
                  </div>
                )}
                {props.selectGradeId===gradeKey && props.selectBlockMap.length>1 && (
                  <ul className={styles.seatZone}>
                     {props.selectBlockMap.map((block,index) =>
                        <li className={styles.liZone}>
                          <a href="#" className={styles.liBlock} onClick={(e) => props.btnBlockClick(e,block.block,gradeKey)}>
                            <div className={styles.seatGrade}>
                              {block.block.blockName}
                            </div>
                          </a>
                        </li>
                     )}
                  </ul>
                )}
            </li>
          ))}
          </ul>
        </div>
        <div className={styles.stopwatchTimer}>
          <p className={styles.time}>
            {Math.floor(props.time / 360000)}:{Math.floor((props.time % 360000) / 6000).toString().padStart(2, "0")}:
            {Math.floor((props.time % 6000) / 100).toString().padStart(2, "0")}:
            {(props.time%100).toString().padStart(2, "0")}
          </p>
        </div>
        <div className={styles.next}>
            {!props.isEnd && (
              <div className={styles.finishBtn}  onClick={(e) => props.clickNext(e)}>
               다음 단계
              </div>
            )}
            {props.isEnd && (
              <div className={styles.finishBtn} onClick={(e) => props.clickReplay(e)} >
               다시 하기
              </div>
            )}
        </div>
      </div>

     
      
    </div>
    
  </div>
);
const CanvasPresenter = (props, ref) => {
  return <canvas ref={props.canvasRef} />;
};

CanvasPresenter.propTypes = {
  canvasRef : PropTypes.object.isRequired,
}
TlBaseball.propTypes = {
  allView : PropTypes.func.isRequired,
  searchText : PropTypes.string.isRequired,
  canvasRef : PropTypes.object.isRequired,
  selectGrade : PropTypes.func.isRequired,
  gradeMap : PropTypes.array.isRequired,
  selectGradeId :  PropTypes.number.isRequired,
  selectBlock : PropTypes.object.isRequired,
  btnGradeClick : PropTypes.func.isRequired,
  selectBlockMap : PropTypes.object.isRequired,
  btnBlockClick : PropTypes.func.isRequired,
  selectGradeMap : PropTypes.array.isRequired,
  popup : PropTypes.bool.isRequired,
  time : PropTypes.number.isRequired,
  popupClose : PropTypes.func.isRequired,
  clickReplay : PropTypes.func.isRequired,
  clickNext : PropTypes.func.isRequired,
  isEnd : PropTypes.bool.isRequired,
  startTimer : PropTypes.func.isRequired,
  istimer : PropTypes.bool.isRequired,
  selectSeat : PropTypes.array.isRequired,
  scale : PropTypes.number.isRequired,
};

export default TlBaseball;