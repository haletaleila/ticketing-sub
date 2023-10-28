import React from "react";
import PropTypes from "prop-types";
import { useParams, Router, Link } from "react-router-dom";
import styles from "./styles.module.scss";
import { TypeAnimation } from "react-type-animation";
import InLeftNav from "../InLeftNav";
import InRightNav from "../InRightNav";
const InMain = ({ onSeatSelection, onConfirm, selectedSeats }) => {
  const { category } = useParams();
  return (
    <div className={styles.container}>
      <div className={styles["flex-container"]}>
        <InLeftNav
          category={category}
          onSeatSelection={onSeatSelection}
          onConfirm={onConfirm}
          selectedSeats={selectedSeats}
        />
        <InRightNav onConfirm={onConfirm} selectedSeats={selectedSeats} />
      </div>
    </div>
  );
};

InMain.propTypes = {
  onSeatSelection: PropTypes.func.isRequired,
  selectedSeats: PropTypes.array.isRequired,
};
export default InMain;
