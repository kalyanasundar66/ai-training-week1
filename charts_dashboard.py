
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load employee data
employees = pd.read_csv("employees.csv")

# Step 2: Create a figure with 4 chart areas
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# ------------------------------------------------
# Chart 1: Average Salary by Department (Bar Chart)
# ------------------------------------------------

avg_salary = employees.groupby("department")["salary"].mean()

bars = axes[0, 0].bar(avg_salary.index, avg_salary.values)

axes[0, 0].set_title("Average Salary by Department")
axes[0, 0].set_xlabel("Department")
axes[0, 0].set_ylabel("Average Salary")

# Display values on bars
for bar in bars:
    height = bar.get_height()
    axes[0, 0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center",
        va="bottom"
    )


# ------------------------------------------------
# Chart 2: Salary Distribution (Histogram)
# ------------------------------------------------

axes[0, 1].hist(
    employees["salary"],
    bins=5,
    edgecolor="black"
)

axes[0, 1].set_title("Salary Distribution")
axes[0, 1].set_xlabel("Salary")
axes[0, 1].set_ylabel("Number of Employees")


# ------------------------------------------------
# Chart 3: Employee ID vs Salary (Scatter Plot)
# ------------------------------------------------

for department in employees["department"].unique():

    department_data = employees[
        employees["department"] == department
    ]

    axes[1, 0].scatter(
        department_data["id"],
        department_data["salary"],
        label=department
    )

axes[1, 0].set_title("Employee ID vs Salary")
axes[1, 0].set_xlabel("Employee ID")
axes[1, 0].set_ylabel("Salary")
axes[1, 0].legend(title="Department")


# ------------------------------------------------
# Chart 4: Monthly Sales (Line Chart)
# ------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

axes[1, 1].plot(
    months,
    sales,
    marker="o",
    label="Monthly Sales"
)

axes[1, 1].set_title("Monthly Sales")
axes[1, 1].set_xlabel("Month")
axes[1, 1].set_ylabel("Sales")
axes[1, 1].legend()
axes[1, 1].grid(True)


# Step 3: Add spacing between charts
plt.tight_layout()

# Step 4: Save the complete dashboard
plt.savefig("all_charts_dashboard.png", dpi=300)

# Step 5: Display the dashboard
plt.show()

print("All four charts displayed in one dashboard!")
