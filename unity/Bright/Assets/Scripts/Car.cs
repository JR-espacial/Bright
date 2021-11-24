using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Car : MonoBehaviour
{
    float speed = 5.0f;
    bool isMoving = true;
    float acumRotation = 0.0f;
    float acumMovement = 0.0f;
    int destination = 2;
    float totalRotation = 0;
    int rotationDirection = 1;
    float totalMovement = 60;
    GameObject car;

    private void Start() {
        
        car = transform.gameObject;

        //Angle for right rotation
        if(destination == 1){
            totalRotation = 90;
        }
        //Angle for left rotation
        else if(destination == 2){
            totalRotation = -90;
            //Rotation direction is negative when rotating left
            rotationDirection = -1;
        }

    }
    void Update()
    {   
        //Rotate when the car has gotten to rotation areas and the total rotation has not been reached
        if(destination == 1 && acumMovement > 23 && acumRotation <= Mathf.Abs(totalRotation)){
            rotate();
        }
        else if(destination == 2 && acumMovement > 27 && acumRotation <= Mathf.Abs(totalRotation)){
            rotate();
        }
        move();
        
    }

    void move(){
        //Moves car -1 x units at a time by speed and delta time
        if(isMoving){
            car.transform.Translate(Vector3.right * Time.deltaTime * speed, Space.Self);
            acumMovement += Mathf.Abs(Vector3.right.x * Time.deltaTime * speed);
            // if(acumMovement >= totalMovement){
            //     Destroy(car);
            //     enabled = false;
            // }
        }
    }

    void rotate(){
        car.transform.Rotate(0, 10f * rotationDirection * Time.deltaTime * speed, 0, Space.World);
        acumRotation += Mathf.Abs(10f * Time.deltaTime * speed);
    }
}
