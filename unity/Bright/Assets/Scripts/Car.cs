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
    float totalMovement = 30;
    [SerializeField] Transform car;

    private void Start() {
        if(destination == 1){
            totalRotation = 90;
        }
        else if(destination == 2){
            totalRotation = -90;
            rotationDirection = -1;
        }

    }
    void Update()
    {   

        if(destination == 1 && acumMovement > 20 && acumRotation <= Mathf.Abs(totalRotation)){
            rotate();
        }
        else if(destination == 2 && acumMovement > 25 && acumRotation <= Mathf.Abs(totalRotation)){
            rotate();
        }
        move();
    }

    void move(){
        if(isMoving){
            // acumMovement += Mathf.Abs(direction * Time.deltaTime * speed);
            // if(acumMovement >= totalMovement){
            //     Destroy(this);
            // }
            car.transform.Translate(Vector3.left*Time.deltaTime*speed, Space.Self);
            acumMovement += Mathf.Abs(Vector3.left.x*Time.deltaTime*speed);
        }
    }

    void rotate(){
        car.transform.Rotate(0, 10f * rotationDirection * Time.deltaTime * speed, 0, Space.World);
        acumRotation += Mathf.Abs(10f * Time.deltaTime * speed);
    }
}
