import Form from 'react-bootstrap/Form';
import button from 'react-bootstrap/Button';
import Button from 'react-bootstrap/Button';
import { Card, Col, Row } from 'react-bootstrap';
import { Navigate, useNavigate } from 'react-router-dom';
import { useState } from 'react';


function Login({email, setEmail, password, setPassword, user, setUser}) {

    const nav = useNavigate()
    return (
        <div>
            <Row>
                <Col></Col>
                <Col>
                <h1 className='mt-5 mb-5 text-center'>Traveler</h1>
                <Form onSubmit={(e) =>  {
                    e.preventDefault()
                    setEmail(e.target[0].value)
                    setPassword(e.target[1].value)
                    fetch('/api/login', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            email: email,
                            password: password
                        })
                    })
                    .then(res => res.json())
                    .then(data => {
                        if (data.error == null) {
                            alert("Login Successful")

                            setUser(data)
                            nav('/trip')

                        } else {
                            alert(data.error)
                        }
                    })
                }}>
                    <Form.Group className='mb-3 mt-5' controlId='loginEmail'>
                        <Form.Label>Email address</Form.Label>
                        <Form.Control type='email' placeholder='Enter email' />
                        <Form.Text className='text-muted'>
                            Enter your registered email address
                        </Form.Text>
                    </Form.Group>

                    <Form.Group className='mb-3' controlId='loginPassword'>
                        <Form.Label>Password</Form.Label>
                        <Form.Control type='password' placeholder='Enter Password' />
                        <Form.Text className='text-muted'>
                            Enter your registered password
                        </Form.Text>
                    </Form.Group>
                    <Button variant='primary' type='submit'  >Login</Button>
                </Form>
                <Button variant='primary' className='mt-3' href='/register'>Register New User</Button>
                </Col>
                <Col></Col>
            </Row>
        </div>
    )
}

export default Login