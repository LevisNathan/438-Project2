import * as React from 'react';

import { Socket } from './Socket';

export class Button extends React.Component {
    constructor(props){
        super(props);
        this.state = {value:''};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    handleChange(event){
        this.setState({value:event.target.value});
    }
    
    handleSubmit(event) {
        event.preventDefault();
        FB.getLoginStatus((response)=>{
            console.log("Checking FB");
            if(response.status=='connected'){
                console.log("Connected to FB");
                Socket.emit('new number', {
                    'facebook_user_token':
                        response.authResponse.accessToken,
                    'number': this.state.value,
                });    
            
            }else{
                alert("You need to be logged in to chat.");
            }
        });
        
    }
    render() {
        return (
                <form onSubmit={this.handleSubmit}>
                <label>
                Enter: 
                <input type="text" value={this.state.value} onChange={this.handleChange} />
                </label>
                <input type="submit" value="Submit"/>
                </form>
                
        );
    }
}
