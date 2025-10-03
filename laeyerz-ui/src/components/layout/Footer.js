import React from 'react'
import {  Row, Col } from 'react-bootstrap'
import {Nav  } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'
import { Container} from 'react-bootstrap'


const Footer = () => {
    return (

        <>
        
        <footer className="footer">
        

        <Container>

        <hr/>

        <Row>
          <Col>
          <LinkContainer to='/termsandconditions'>
                    <Nav.Link> 
                    <span style={{color:'black'}}>Terms and Conditions</span>
                    </Nav.Link>
            </LinkContainer>
          
          </Col>
          <Col>
          <LinkContainer to='/privacypolicy'>
                <Nav.Link> 
                <span style={{color:'black'}}>Privacy Policy</span>
                </Nav.Link>
            </LinkContainer>
          
          </Col>
          <Col>
          
             
              <span style={{color:'black'}}>pixagan@gmail.com</span>
             
            
         
          </Col>
        </Row>

        <hr/>

        <Row>
          <Col className='text-center py-3 mt-0'>
          <span> &copy; 2025-, Pixagan Technologies Pvt Limited. All rights reserved. | </span>
          </Col>
        </Row>

        <hr />

        </Container>





        </footer>
        
        </>


        )
    }
    
    export default Footer