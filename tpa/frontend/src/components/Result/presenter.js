import React from "react";
import PropTypes from "prop-types";
import {Router,Link } from "react-router-dom";
import styles from "./styles.module.scss";
import { TypeAnimation } from 'react-type-animation';
const Main = (props, context) => (
  <>
    {props.card.length>0 && (
      <>
      {props.card.map((cd,idx) => 
        <Cards cd={cd} idx={idx+1} cardClick={props.cardClick} />
      )}
      </>
    )}
  </>
  );
const Cards = (props,context)=>(
  <>
    {props.cd.length > 0 && (
      <div className={styles.card}>
        <div className={styles.name}>
          <TypeAnimation
              sequence={[
                '',
                500, 
                props.cd[0].text_content,
                500, 
                () => {
                  
                },
              ]}
              wrapper="span"
              deletionSpeed={30}
              cursor={true}
              repeat={Infinity}
              style={{ fontSize: '28px', display: 'inline' }}
            />
        </div>
        
        
         {chunkArray(props.cd, 4).map((chunk, chunkIndex) => (
        <div className={styles.images}>
          {chunk.map((cardinfo, index) => (
            <div 
              key={index}
              style={{marginLeft: (props.cd.length <= 4 ? 80/props.cd.length : 80/4) + "px",
              marginRight: (props.cd.length <= 4 ? 80/props.cd.length : 80/4) + "px"}}
              tabIndex="0" 
              className={styles.itemView} 
              onClick={() => props.cardClick(cardinfo.children, props.idx, cardinfo)}
            >  
              <div className={styles.contentWithImg}>
                <img 
                  width={800/(props.cd.length <= 4 ? props.cd.length : 4)} 
                  height={1000/(props.cd.length <= 4 ? props.cd.length : 4)} 
                  alt="" 
                  src={cardinfo.image} 
                  className={styles.cardImgFull}
                />
                <div className={styles.contentInfo}>
                  <h3 className={styles.title}>{cardinfo.title}</h3>
                </div>
              </div>
            </div>
          ))}
        </div>
      ))}
        </div>
    )}
  </>
)
function chunkArray(array, size) {
  const chunked = [];
  for (let i = 0; i < array.length; i += size) {
    chunked.push(array.slice(i, i + size));
  }
  return chunked;
}
const TestButton = (props,context) => (
  <>
    {

    }
    
  </>
)

Main.propTypes = {
  card:PropTypes.array.isRequired,
  cardClick: PropTypes.func.isRequired,
};

Cards.propTypes = {
  cd:PropTypes.array.isRequired,
  cardClick: PropTypes.func.isRequired,
};

export default Main;