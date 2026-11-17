
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the employee data from CSV file
employees = pd.read_csv("employees.csv")

# Display the employee data
print(employees)

# ------------------------------------------------
# Chart 1: Average Salary by Department (Bar Chart)
# ------------------------------------------------

# Calculate average salary for each department
avg_salary = employees.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))

# Draw the bar chart
bars = plt.bar(avg_salary.index, avg_salary.values)

# Add title and axis labels
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# Display salary values on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("average_salary_by_department.png")
plt.show()


# ------------------------------------------------
# Chart 2: Salary Distribution (Histogram)
# ------------------------------------------------

plt.figure(figsize=(8, 5))

# Create histogram with 5 bins
plt.hist(employees["salary"], bins=5, edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("salary_distribution.png")
plt.show()


# ------------------------------------------------
# Chart 3: Employee ID vs Salary (Scatter Plot)
# ------------------------------------------------

plt.figure(figsize=(8, 5))

# Draw scatter points for each department
for department in employees["department"].unique():

    department_data = employees[
        employees["department"] == department
    ]

    plt.scatter(
        department_data["id"],
        department_data["salary"],
        label=department
    )

plt.title("Employee ID vs Salary by Department")
plt.xlabel("Employee ID")
plt.ylabel("Salary")

# Display department names
plt.legend(title="Department")

plt.tight_layout()
plt.savefig("employee_id_vs_salary.png")
plt.show()


# ------------------------------------------------
# Chart 4: Monthly Sales (Line Chart)
# ------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

# Draw line chart with markers
plt.plot(
    months,
    sales,
    marker="o",
    linestyle="-",
    label="Monthly Sales"
)

plt.title("Monthly Sales from January to June")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()


# ------------------------------------------------
# Final Message
# ------------------------------------------------

print("All 4 charts have been saved successfully!")
