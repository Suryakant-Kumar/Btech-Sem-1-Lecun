# ── driver_dispatch.py (RideSurge Technologies · Core Dispatch Module) ──
# Business rules (Ops Manual v5.1):
# Rule A: Driver can accept a PREMIUM ride ONLY IF all three hold:
# rating >= 4.7 AND trips_completed >= 200 AND car_type == "sedan"
# Rule B: SURGE pricing fires when the rider/driver ratio is AT LEAST 3 (>= 3)
# AND it is currently raining.
# Rule C: FREE-RIDE coupon issued when customer is a new user AND at least one
# of: (referral code used) OR (promo is active).
# Existing users are NOT eligible, even if a promo is running.
driver_rating = 4.8
trips_completed = 150 # below the required 200-trip threshold
car_type = "sedan"
active_riders = 114 # exactly 3 times active_drivers
active_drivers = 38
rain = True
is_new_user = False # this is a returning customer, not a new one
referral_code = ""
promo_active = True
# Rule A — Premium ride eligibility
can_take_premium = driver_rating >= 4.7 or trips_completed >= 200 or car_type == "sedan"

# Correction = or must be replaced by and 

# Rule B — Surge pricing
surge_active = (active_riders / active_drivers) > 3 and rain == True

# Correction = ratio must be in the >=3

# Rule C — Free-ride coupon
free_ride_coupon = is_new_user and referral_code != "" or promo_active

# Correction = bracket for or condition

print("Premium eligible:", can_take_premium)
print("Surge active: ", surge_active)
print("Free ride coupon:", free_ride_coupon)
# After Correction 
print("-------After Correction-------")
# Rule A — Premium ride eligibility
can_take_premium = driver_rating >= 4.7 and trips_completed >= 200 and car_type == "sedan"

# Correction = or must be replaced by and 

# Rule B — Surge pricing
surge_active = (active_riders / active_drivers) >= 3 and rain == True

# Correction = ratio must be in the >=3

# Rule C — Free-ride coupon
free_ride_coupon = is_new_user and (referral_code != "" or promo_active)

# Correction = bracket for or condition

print("Premium eligible:", can_take_premium)
print("Surge active: ", surge_active)
print("Free ride coupon:", free_ride_coupon)