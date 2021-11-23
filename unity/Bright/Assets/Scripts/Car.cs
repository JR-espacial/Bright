using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Car : MonoBehaviour
{
    float speed = 5.0f;
    bool isMoving = true;
    bool isRotating = false;
    float acumRotation = 0.0f;
    float acumMovement = 0.0f;
    int destination = 1;
    float totalRotation = 0;
    float totalMovement = 30;
    // 1 for positive, -1 for negative
    int direction = 1;
    //0 for x, 1 for z
    bool currentAxis = false;
    [SerializeField] Transform car;

    private void Start() {
        Debug.Log("start");
        Debug.Log(car.transform.rotation.eulerAngles);
        if(destination == 1){
            totalRotation = 90;
        }
        else if(destination == 2){
            totalRotation = -90;
        }
        if(car.transform.rotation.eulerAngles.y == 270){
            Debug.Log(90);
            currentAxis = true;
            direction = 1;
        }
        else if(car.transform.rotation.eulerAngles.y == 90){
            Debug.Log(-90);
            currentAxis = true;
            direction = -1;
        }
        else if(car.transform.rotation.eulerAngles.y == 180){
            Debug.Log(0);
            currentAxis = false;
            direction = -1;
        }
        else if(car.transform.rotation.eulerAngles.y == 0){
            Debug.Log(180);
            currentAxis = false;
            direction = 1;
        }

    }
    void Update()
    {   

        if(acumMovement > 15 && acumRotation <= Mathf.Abs(totalRotation)){
            rotate();
        }
        if(acumRotation >= Mathf.Abs(totalRotation)){

            if(currentAxis){
                if(destination == 1){
                    direction = destination * -1;
                }
                else if(destination == 2){
                    direction = destination * 1;
                }
                currentAxis = false;
            }
            else{
                if(destination == 1){
                    direction = destination * 1;
                }
                else if(destination == 2){
                    direction = destination * -1;
                }
                currentAxis = true;
            }
        }
        move();
    }

    void move(){
        if(isMoving){
            // if(currentAxis == false){
            //     car.transform.position += new Vector3(direction * Time.deltaTime * speed, 0, 0);
            // }
            // else{
            //     car.transform.position += new Vector3(0, 0, direction * Time.deltaTime * speed);
            // }
            // acumMovement += Mathf.Abs(direction * Time.deltaTime * speed);
            // if(acumMovement >= totalMovement){
            //     Destroy(this);
            // }

            
            car.transform.Translate(Vector3.left*Time.deltaTime*speed, Space.Self);
            
            acumMovement += Mathf.Abs(Vector3.left.x*Time.deltaTime*speed);
        }
    }

    void rotate(){
        car.transform.Rotate(0, 10f * Time.deltaTime * speed, 0, Space.World);
        acumRotation += Mathf.Abs(10f * Time.deltaTime * speed);
    }
}
