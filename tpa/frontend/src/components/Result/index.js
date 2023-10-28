import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as cardActions } from "../../redux/modules/card"

const mapStateToProps = (state, ownProps) => {
  const { card :{card} } = state;
  return {
    card,
  };
};

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    
    getCard : () => {
      dispatch(cardActions.getCard());
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Container);