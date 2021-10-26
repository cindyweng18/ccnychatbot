import React, {useState} from 'react';
import './Chat.css'

const Chat =(props)=>{
    const {convo} = props

    return (
        <div className='paper'>
            {convo.map(item =>
                <>
                    <div className='chat-mes'>
                        {item.mes}
                    </div>
                    <div className='chat-res'>
                        {item.res}
                    </div>
                </>
            )}
        </div>
    );
}
export default Chat