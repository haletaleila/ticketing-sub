const SET_CATEGORY = "SET_CATEGORY";
const SET_ITEM = "SET_ITEM";

export const setCategory = (category) => ({
  type: SET_CATEGORY,
  category,
});

export const setItem = (item) => ({
  type: SET_ITEM,
  item,
});

const initialState = {
  category: null,
  item: null,
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_CATEGORY:
      return { ...state, category: action.category, item: null }; // Reset item when category changes
    case SET_ITEM:
      return { ...state, item: action.item };
    default:
      return state;
  }
};

export default reducer;
