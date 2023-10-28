import React from "react";
import PropTypes from "prop-types";
import {Router,Link } from "react-router-dom";
import styles from "./styles.module.scss";
import { TypeAnimation } from 'react-type-animation';
const Preparing = (props,context)=>(
  <>
     <div className={styles.comingSoon}>
        <img src={require("../../images/logo.png")} alt="" className={styles.logo}/>
        <h1 className={styles.pc}>PC에서 이용해주시기 바랍니다.</h1>
        <p className={styles.explain}>티켓랩은 가로 980px 세로 600px 이상 환경에서 지원합니다.</p>
      </div>
  </>
)
Preparing.propTypes = {
};

export default Preparing;