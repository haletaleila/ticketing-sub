import React from "react";
import PropTypes from "prop-types";
import {Router,Link } from "react-router-dom";
import styles from "./styles.module.scss";
import store, { history } from "../../redux/configureStore"
const Footer = (props, context) => (
  <div className={styles.Footer}>
        <div className={styles.description}>
            <div className={styles.name}>
              티켓팅 연습은 Ticket Lab
            </div>
            <div className={styles.explain}>
              모든 티켓팅 연습의 이미지의 저작권은 해당 사이트에 있습니다.
            </div>
            <div className={styles.company}>
              © 2023 Project Lophorina SoftTech
            </div>
        </div>
  </div>
);

Footer.propTypes = {
};


export default Footer;