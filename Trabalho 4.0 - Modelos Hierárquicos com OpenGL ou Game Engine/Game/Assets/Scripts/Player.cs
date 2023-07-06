using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{   

    private CharacterController controller;
    private Animator anim;

    public float walkSpeed;
    public float runSpeed;
    public float gravit;
    public float rotSpeed;

    private float rot;
    private Vector3 moveDirection;

    // Start is called before the first frame update
    void Start()
    {
        controller = GetComponent<CharacterController>();
        anim = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        Animation();
        Move();
        

    }

    void Animation(){

        if(Input.GetKeyDown(KeyCode.Alpha1)){
            anim.SetInteger("transition", 3);
        }

        if(Input.GetKeyDown(KeyCode.Alpha2)){
            anim.SetInteger("transition", 4);
        }

        if(Input.GetKeyDown(KeyCode.Alpha3)){
            anim.SetInteger("transition", 5);
        }

        if(Input.GetKeyDown(KeyCode.Alpha4)){
            anim.SetInteger("transition", 6);
        }
        if(Input.GetKeyDown(KeyCode.Alpha5)){
            anim.SetInteger("transition", 7);
        }

        if(Input.GetKeyDown(KeyCode.Alpha6)){
            anim.SetInteger("transition", 8);
        }

        if(Input.GetKeyDown(KeyCode.Alpha7)){
            anim.SetInteger("transition", 9);
        }
        
        if(Input.GetKeyDown(KeyCode.Alpha8)){
            anim.SetInteger("transition", 10);
        }
        
        if(Input.GetKeyDown(KeyCode.Alpha9)){
            anim.SetInteger("transition", 11);
        }
        
        if(Input.GetKeyDown(KeyCode.Alpha0)){
            anim.SetInteger("transition", 12);
        }

    }

    void Move()
    {
        if(controller.isGrounded)
        {
            if(Input.GetKey(KeyCode.W)){
                if(Input.GetKey(KeyCode.Space)){
                    moveDirection = Vector3.forward * runSpeed;
                    anim.SetInteger("transition", 2);
                }
                else {
                    moveDirection = Vector3.forward * walkSpeed;
                    anim.SetInteger("transition", 1);
                }
            }

            if(Input.GetKeyUp(KeyCode.W)){
               moveDirection = Vector3.zero;
                anim.SetInteger("transition", 0);
            }
        }

        rot += Input.GetAxis("Horizontal") * rotSpeed * Time.deltaTime;
        transform.eulerAngles = new Vector3(0,rot,0);

        moveDirection.y -= gravit * Time.deltaTime;
        moveDirection = transform.TransformDirection(moveDirection);

        controller.Move(moveDirection * Time.deltaTime);
    }
}
