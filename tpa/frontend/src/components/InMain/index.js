import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as cardActions } from "../../redux/modules/card";
import { setCategory, setItem } from "../../redux/modules/incategory";

const mapStateToProps = (state, ownProps) => {};

const mapDispatchToProps = (dispatch) => ({});

export default connect(mapStateToProps, mapDispatchToProps)(Container);
