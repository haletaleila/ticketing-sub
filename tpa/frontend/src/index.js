import React from 'react';
import ReactDOM from 'react-dom';
import Helmet from 'react-helmet';
import {Provider} from "react-redux";
import store, {history} from "./redux/configureStore";
import {ConnectedRouter} from "connected-react-router";

import './index.css';
import App from './components/App';

ReactDOM.render(
    
    <Provider store={store}>
        <Helmet>
        <script src="https://code.jquery.com/jquery-latest.js"></script> 
                <meta name="description" content="티켓팅 연습은 티켓랩.COM - LOPHORINA SOFTTech" data-react-helmet="true"/>
            </Helmet>
        <ConnectedRouter history={history}>
        <App />
       
        </ConnectedRouter>
    </Provider>, 
    document.getElementById('root')
);
