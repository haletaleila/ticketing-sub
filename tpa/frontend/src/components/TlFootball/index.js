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
    getFootballBlockObj : (eng) => {
      dispatch(ticketingActions.getFootballBlockObj(eng));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Container);