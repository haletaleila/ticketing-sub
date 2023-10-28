import React from "react";
import PropTypes from "prop-types";
import {Router,Link } from "react-router-dom";
import styles from "./styles.module.scss";
import { TypeAnimation } from 'react-type-animation';
const CaptchaGame = (props,context)=>(
  <>
    <div className={styles.main}>
    <div className={styles.top}>
      {!props.isTimer&& (
        <>
          <div className={styles.explain1}>
            입력 부분을 클릭하면 타이머가 시작됩니다.
          </div>
          <div className={styles.explain2}>
            캡챠를 통과할 때마다 제한시간이 2초씩 늘어납니다.
          </div>
          </>
      )}
      {props.isTimer&& (
        <>  
         <div className={styles.stopwatchTimer}>
          <p className={styles.time}>
            {Math.floor(props.time / 360000)}:{Math.floor((props.time % 360000) / 6000).toString().padStart(2, "0")}:
            {Math.floor((props.time % 6000) / 100).toString().padStart(2, "0")}:
            {(props.time%100).toString().padStart(2, "0")}
          </p>
        </div>
        </>
      )}
    </div>

      <div className={styles.gameBoard}>
        <div className={styles.reload}>
          <button onClick={props.reload} type="button" title="새로고침">
            <span >새로고침</span>
          </button>
        </div>
        
        <div id="container"  className={styles.CaptchaContainer}>
          <canvas id="overlay"></canvas>
          <div id="captcha" className={styles.Captcha}></div>
        </div>
        <div className={styles.inputContainer}>
          <input placeholder="문자를 입력해주세요" type="text" onFocus={props.handleFocus} value={props.inputValue} onKeyDown={props.handleKeyDown} onChange={props.handleChange} className={styles.captchaInput}/>
        </div>
      </div>
      <div className={styles.bottom}>
        <div className={styles.score}>
            LV : {props.score} 단계
          </div>
      </div>
    </div>
    
  </>
)
CaptchaGame.propTypes = {
  handleChange : PropTypes.func.isRequired,
  handleKeyDown : PropTypes.func.isRequired,
  reload : PropTypes.func.isRequired,
  handleFocus : PropTypes.func.isRequired,
  inputValue : PropTypes.string.isRequired,
  time : PropTypes.number.isRequired,
  isTimer : PropTypes.bool.isRequired,
  score : PropTypes.number.isRequired,
};

export default CaptchaGame;