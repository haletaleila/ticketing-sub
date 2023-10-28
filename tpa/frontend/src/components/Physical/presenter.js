import React from "react";
import PropTypes from "prop-types";
import {Router,Link } from "react-router-dom";
import styles from "./styles.module.scss";
import { TypeAnimation } from 'react-type-animation';
const Physical = (props, context) => (
  <div className={styles.main}>
    <div className={styles.card}>
        <div className={styles.name}>
          <TypeAnimation
              sequence={[
                "연습을 진행할 카테고리를 선택해주세요",
                500, 
                () => {
                  
                },
              ]}
              wrapper="span"
              deletionSpeed={30}
              cursor={true}
              repeat={Infinity}
              style={{ fontSize: '28px', display: 'inline' }}
            />
        </div>
        <div className={styles.images}>
          <a href="/tlrandomgame">
            <div className={styles.itemView} >  
              <div className={styles.contentWithImg}>
                <img 
                  width={400} 
                  height={500} 
                  alt="" 
                  src={require("../../images/tlrandom.JPG")} 
                  className={styles.cardImgFull}
                />
                <div className={styles.contentInfo}>
                  <h3 className={styles.title}>T사 랜덤 좌석 선택 게임</h3>
                </div>
              </div>
            </div>
            </a>
            <a href="/captcha">
              <div className={styles.itemView} >  
                <div className={styles.contentWithImg}>
                  <img 
                    width={400} 
                    height={500} 
                    alt="" 
                    src={require("../../images/captcha.JPG")} 
                    className={styles.cardImgFull}
                  />
                  <div className={styles.contentInfo}>
                    <h3 className={styles.title}>캡챠 연습 게임</h3>
                  </div>
                </div>
              </div>
            </a>
        </div>
    </div>
  </div>
);
function chunkArray(array, size) {
  const chunked = [];
  for (let i = 0; i < array.length; i += size) {
    chunked.push(array.slice(i, i + size));
  }
  return chunked;
}

Physical.propTypes = {
  card:PropTypes.array.isRequired,
  cardClick: PropTypes.func.isRequired,
};


export default Physical;