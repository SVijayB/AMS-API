import React, {Component} from 'react';

//Constants

class Notification extends Component {
    handleClick = this.handleClick.bind(this);
    handleClick(props){
        if(this.props.authenticated) {
            alert('You are logged in. There is nothing more to do except hire Shelton :). Alternatively, refresh the browser.')
        } else {
            document.getElementById('popup-wrapper').classList.remove("visible");
            document.getElementById('popup-wrapper').classList.add("hidden");
        };
    };
    render(props){
        return(
            <div id="popup-wrapper" className="hidden">
                <div id="information-popup" className="pop-up">
                    <h4 id="popup-title" style={{color:this.props.responseColor ,textAlign: 'center'}}>{this.props.response}</h4>
                    <p id="popup-message">{this.props.message}</p>
                    <button id="popup-action" className="btn button-color" onClick={this.handleClick}>{this.props.buttonText}</button>
                </div>
            </div>
        );
    };
};

export default Notification;