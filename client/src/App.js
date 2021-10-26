import React, {useState, useEffect,useRef } from 'react'

import Container from '@mui/material/Container';

import Header from './components/header/Header';
import Chat from './components/chat/Chat';
import MessageBox from './components/messageBox/MessageBox'
import ChatBubbleOutlineIcon from '@mui/icons-material/ChatBubbleOutline';

const App =()=> {

  const sampleConvo=[
    {mes:'Hey',res:'Hi!'},
    {mes:'Can you help me?',res:'Yes.'},
    {mes:'What is the ccny website link?',res:'Please visit https://www.ccny.cuny.edu/'},
    {mes:'Thanks',res:'You are welcome!'},
  ]
  const [convo, setConvo] = useState([])
  const [isOpen, setIsOpen] = useState(false)

  const ref = useRef()
  useEffect(() => {
    setConvo(sampleConvo)
  },[])

  const handleClick = (e) => {

    e.preventDefault();
    //TODO: Get response from ML model using mes.
    let newConvo= [...convo]
    newConvo.push({mes:ref.current.value,res:`random response ${Math.floor(Math.random() * 20)}`})
    setConvo(newConvo)
    ref.current.value = ""

  }

  const openModal = ()=> {
    setIsOpen(!isOpen)
  }

  return (
    <>
    {isOpen ?
    <Container component="main" maxWidth="xs"style={{bottom:150,right:150,position:'absolute' }}>
      <div style={{ boxShadow: '0px 0px 50px #a7a7a7', borderRadius: '1rem 1rem 1rem 1rem'}}>
        <Header openModal={openModal}/>
        <Chat convo={convo}/>
        <MessageBox handleClick={handleClick} ref={ref}/>
      </div>
    </Container>
    
    :
    <div onClick={openModal}>
      <ChatBubbleOutlineIcon sx={{ color: 'white',backgroundImage: 'linear-gradient(to right, #6e0fc8, #cd49e6)',fontSize:'5rem',borderRadius:'50%',padding:'2rem',bottom:50,right:50,position:'absolute' }}/>
    </div>
    }
    </>
  )
}

export default App
