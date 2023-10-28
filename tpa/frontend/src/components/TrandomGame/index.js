import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as ticketingActions } from "../../redux/modules/ticketing"

const mapStateToProps = (state, ownProps) => {
  const { ticketing :{randomobj} } = state;
  return {
    randomobj,
  };
};
const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    getRandomTicketLink : () => {
      dispatch(ticketingActions.getRandomTicketLink());
    },
  };
};
export default connect(mapStateToProps, mapDispatchToProps)(Container);