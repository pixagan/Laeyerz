import './App.css';

import React from 'react'


import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';


import Footer from './components/layout/Footer'

import FlowScreen from './screens/FlowScreen'



const App = () => {


  return (

    <div className="app-flex-root">

      <Router>

        <main  style={{marginTop:'0px', paddingTop:'0px', flex: '1 0 auto'}}>

          <Routes>
               
            <Route path='/' element={<FlowScreen />} exact /> 

          </Routes>

        </main>

        <Footer />

      </Router>

    </div>

  );
}

export default App;



