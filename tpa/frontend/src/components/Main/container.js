import React, { Component } from "react";
import PropTypes from "prop-types";
import Main from "./presenter";

class Container extends Component {
  state = {
    card : [],
    selectedCardIndex : -1,
  };
  
  static propTypes = {
    getCard : PropTypes.func.isRequired,
    card : PropTypes.array.isRequired,
  };
  componentWillReceiveProps = nextProps => {
    if(nextProps.card ){
      if(this.state.card.length==0){
        this.setState({
          card : [nextProps.card],
        })
      }
  	}
  };
  cardClick = (children, index, card) => {
    if(card.isPreparing){
      alert("해당 메뉴는 준비 중입니다.")
    }
    else{
      if(card.isGoods){
        window.location.href = card.url;
      }
      else{
        let updatedCards = [...this.state.card];
        updatedCards.splice(index);
        if (updatedCards.length > 0 ) {
            updatedCards.push(children); 
        }
        this.setState({ card: updatedCards }, () => {
          window.scrollTo({
              top: document.body.scrollHeight,
              behavior: "smooth"
          });
      });
      }
    }
}
  componentDidMount() {
    document.title = "티켓랩(TicketLab)";
    const {getCard } = this.props;
    getCard();
  };
  render() {
    return (
      <>
      <Main cardClick={this.cardClick} {...this.state} onKeyPress={this.onKeyPress} />
      </>
    );
  }
}

export default Container;