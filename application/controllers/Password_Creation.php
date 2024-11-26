<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Password_Creation extends CI_Controller {

	/**
	 * Index Page for this controller.
	 *
	 * Maps to the following URL
	 * 		http://example.com/index.php/welcome
	 *	- or -
	 * 		http://example.com/index.php/welcome/index
	 *	- or -
	 * Since this controller is set as the default controller in
	 * config/routes.php, it's displayed at http://example.com/
	 *
	 * So any other public methods not prefixed with an underscore will
	 * map to /index.php/welcome/<method_name>
	 * @see https://codeigniter.com/userguide3/general/urls.html
	 */
	public function index()
	{
		
	}
    public function create_password($plain_password,$check_password)
    {
        $hashed_password = password_hash($plain_password,PASSWORD_DEFAULT);
        $this -> load ->view('header');
        
        #$this->load->library('parser');
		#$this->load->parser->parse('password_hashing',$plain_password,$hashed_password);
        echo $plain_password;
        echo "<br>";
        echo $hashed_password;
        echo "<br>";
        if(password_verify($check_password,$hashed_password))
        {
                echo "Passwords match! Password is ", $check_password;
        }
        else
        {
            echo "Passwords don't match! Password is not ", $check_password;
        }
        $this-> load -> view('footer');

    }
	
}
