import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as ticketingActions } from "../../redux/modules/ticketing"

const mapStateToProps = (state, ownProps) => {
  const { ticketing :{blockobj} } = state;
  return {
    blockobj,
  };
};

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    getBaseballBlockObj : (eng) => {
      dispatch(ticketingActions.getBaseballBlockObj(eng));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Container);