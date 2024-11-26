<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Special_Controller extends CI_Controller {

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
    public function special_test($name,$number, $subtract)
    {
        $this->load->view('header');
        #$this -> load->view('level_test');
		$diff = $number - $subtract;

		$this->load->library('parser');
		$this->load->parser->parse('level_test',$number);
		
		#echo "No help variable: <br> Name: " . $name . "<br> First number: " . $number . "<br> Second number: " . $subtract . "<br> Difference: " . ($number-$subtract);
		#echo "<br> <h3>Help variable: </h3> <br>" . $name . "<br> <h5>" . $diff . "</h5>";
		
        $this->load->view('footer');
    }
	
}
