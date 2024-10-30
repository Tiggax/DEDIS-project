<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Custom_welcome extends CI_Controller {
	public function index()
	{
		$this->load->view('templates/custom_welcome');
	}
}
