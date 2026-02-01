<!-- app/templates/application.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Velvoro OS - Application</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
        }
        .form-box {
            width: 420px;
            margin: 80px auto;
            padding: 30px;
            background: #ffffff;
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-top: 12px;
        }
        input, textarea {
            width: 100%;
            padding: 8px;
            margin-top: 6px;
        }
        button {
            margin-top: 20px;
            width: 100%;
            padding: 10px;
            background: #2563eb;
            color: #ffffff;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="form-box">
        <h2>Application Form</h2>

        <form method="post" action="/application">
            <label>Customer Name</label>
            <input type="text" name="customer_name" required>

            <label>Mobile Number</label>
            <input type="text" name="mobile_number" required>

            <label>Email ID</label>
            <input type="email" name="email" required>

            <label>Location / Address</label>
            <textarea name="location" rows="3" required></textarea>

            <button type="submit">Submit Application</button>
        </form>
    </div>
</body>
</html>
