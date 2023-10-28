import React from "react";
import PropTypes from "prop-types";
import {Router,Link } from "react-router-dom";
import styles from "./styles.module.scss";
import store, { history } from "../../redux/configureStore"
const customStyles = {
  content: {
    top: '50%',
    left: '50%',
    right: 'auto',
    bottom: 'auto',
    marginRight: '-50%',
    transform: 'translate(-50%, -50%)',
  },
};
const TopNav = (props, context) => (
  <div className={styles.TopNav}>
        <div className={styles.item}>
          <a href="/">
            <img src={require("../../images/logo.png")} alt="" className={styles.logo}/>
          </a>
          <ul className={styles.menu}>
            <a href="/">
              <li className={styles.menuli}>
                  티켓팅 연습
              </li>
            </a>
            <a href="/physical">
              <li className={styles.menuli}>
                  피지컬 연습
              </li>
            </a>
            <li className={styles.menuli} onClick={(e) => alert("해당 메뉴는 준비 중입니다.")}>
                좌석 VIEW
            </li>
            <li className={styles.menuli} onClick={(e) =>  alert("해당 메뉴는 준비 중입니다.")}>
                요청 게시판
            </li>
          </ul>
        </div>
        
  </div>
);

TopNav.propTypes = {
};

TopNav.contextTypes = {
};

export default TopNav;