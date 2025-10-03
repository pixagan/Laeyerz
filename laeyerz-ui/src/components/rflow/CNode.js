import { useCallback } from 'react';
import { Card, Badge, InputGroup, Button } from 'react-bootstrap'
import { Handle } from '@xyflow/react';

export function CNode(props) {
    const onChange = useCallback((evt) => {
      console.log(evt.target.value);
    }, []);
   
    return (
      <div className="text-updater-node" style={{borderRadius:'10px'}}>
        <Card style={{padding:'5px', borderRadius:'10px', minWidth:'200px', margin:'5px'}}>
          <Card.Header style={{padding:'2px', textAlign:'center'}}>
            <p className='h5'>{props.data.label}</p>
          </Card.Header>
          <Card.Body style={{padding:'2px', textAlign:'center'}}>
            <span className='h6' style={{color:'blue'}}>{props.data.type}</span>
            {props.data.subtype && (
              <span className='h6' style={{color:'blue'}}> - {props.data.subtype}</span>
            )}
            
          </Card.Body>
          
      
        </Card>

            <Handle type="source" position="bottom" />
            <Handle type="target" position="top" />
      </div>
    );
  }