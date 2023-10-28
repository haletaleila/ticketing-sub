import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as cardActions } from "../../redux/modules/card"

const mapStateToProps = (state, ownProps) => {
  return {
  };
};

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Container);