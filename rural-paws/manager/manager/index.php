<?php include('functions.inc.php'); ?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../docs-assets/ico/favicon.png">

    <title>Rural PAWS Manager</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="manager.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy this line! -->
    <!--[if lt IE 9]><script src="../../docs-assets/js/ie8-responsive-file-warning.js"></script><![endif]-->

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Rural PAWS Manager</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li><a href="/">Home</a></li>
            <li class="active"><a href="/manager/">Manager</a></li>
            <li><a href="/manager/settings.php">View Settings</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container">

      <div class="starter-template">
        <h1>Global Settings</h1>
        <p class="lead">Settings set here will apply to all deployed Rural PAWS routers.</p>
<form role="form">
  <div class="form-group">
    <label for="deviceSpeed">Device speed (Bps)</label>
    <input type="text" class="form-control" id="deviceSpeed" placeholder="Device speed (Bps)" value="<?php echo(getDeviceSpeed()); ?>">
  </div>
  <div class="form-group">
    <label for="linkSpeed">Link speed (Bps)</label>
    <input type="text" class="form-control" id="linkSpeed" placeholder="Device speed (Bps)" value="<?php echo(getLinkSpeed()); ?>">
  </div>
  <div class="form-group">
    <label for="deviceSpeed">Approved domains (one per line)</label>
    <textarea id="approvedDomains" placeholder="Approved Domains" class="form-control" rows="20"><?php foreach ( getApprovedDomains() as $domain ) { echo $domain."\n"; } ?></textarea>
  </div>
  <button type="submit" class="btn btn-default">Save Settings</button>
</form>

      </div>

    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
  </body>
</html>

